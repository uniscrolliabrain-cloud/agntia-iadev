import {searchInputSchema,contextInputSchema,sourceIdSchema,curriculumResponseSchema,searchResponseSchema,sourceResponseSchema,contextResponseSchema,healthResponseSchema} from "./contracts.js";
export type KnowledgeErrorKind="auth"|"forbidden"|"not_found"|"validation"|"unavailable"|"timeout"|"contract"|"rate_limit";
export class KnowledgeError extends Error {
 constructor(readonly kind:KnowledgeErrorKind,readonly status:number,readonly retryable=false){super("Knowledge SDK: "+kind);this.name="KnowledgeError";}
}
type Options={baseUrl:string;approvedOrigins:readonly string[];credential:()=>string|Promise<string>;timeoutMs?:number;fetch?:typeof fetch};
export class KnowledgeClient {
 readonly #base:URL;readonly #credential:Options["credential"];readonly #fetch:typeof fetch;readonly #timeout:number;
 constructor(o:Options){
  if(typeof window!=="undefined")throw new KnowledgeError("forbidden",403);
  let u:URL;try{u=new URL(o.baseUrl);}catch{throw new KnowledgeError("validation",422);}
  if(!o.approvedOrigins.includes(u.origin)||u.username||u.password||u.search||u.hash||u.pathname!=="/"||!(u.protocol==="https:"||(u.protocol==="http:"&&["localhost","127.0.0.1","[::1]"].includes(u.hostname))))throw new KnowledgeError("validation",422);
  this.#base=u;this.#credential=o.credential;this.#fetch=o.fetch??fetch;this.#timeout=o.timeoutMs??5000;
  if(!Number.isInteger(this.#timeout)||this.#timeout<10||this.#timeout>30000)throw new KnowledgeError("validation",422);
 }
 async #request<T>(method:"GET"|"POST",path:string,parse:(v:unknown)=>T,body?:unknown):Promise<T>{
  const controller=new AbortController();const timer=setTimeout(()=>controller.abort(),this.#timeout);
  try{
   const token=await this.#credential();
   if(typeof token!=="string"||!/^[\x21-\x7E]{24,512}$/.test(token))throw new KnowledgeError("auth",401);
   const url=new URL(path,this.#base);if(url.origin!==this.#base.origin)throw new KnowledgeError("validation",422);
   const response=await this.#fetch(url,{method,headers:{Authorization:"Bearer "+token,Accept:"application/json","X-Correlation-ID":crypto.randomUUID(),...(body===undefined?{}:{"Content-Type":"application/json"})},body:body===undefined?undefined:JSON.stringify(body),redirect:"error",cache:"no-store",signal:controller.signal});
   if(!response.headers.get("content-type")?.includes("application/json"))throw new KnowledgeError("contract",502);
   if(Number(response.headers.get("content-length")??0)>1048576){await response.body?.cancel();throw new KnowledgeError("contract",502);}
   if(!response.body)throw new KnowledgeError("contract",502);
   const reader=response.body.getReader();const chunks:Uint8Array[]=[];let size=0;
   while(true){const {done,value}=await reader.read();if(done)break;size+=value.byteLength;if(size>1048576){await reader.cancel();throw new KnowledgeError("contract",502);}chunks.push(value);}
   const bytes=new Uint8Array(size);let offset=0;for(const chunk of chunks){bytes.set(chunk,offset);offset+=chunk.byteLength;}
   let payload:unknown;try{payload=JSON.parse(new TextDecoder("utf-8",{fatal:true}).decode(bytes));}catch{throw new KnowledgeError("contract",502);}
   if(!response.ok){const status=response.status;throw new KnowledgeError(status===401?"auth":status===403?"forbidden":status===404?"not_found":status===429?"rate_limit":status===400||status===422?"validation":"unavailable",status,status===429||status>=500);}
   try{return parse(payload);}catch{throw new KnowledgeError("contract",502);}
  }catch(e){if(e instanceof KnowledgeError)throw e;throw new KnowledgeError(controller.signal.aborted?"timeout":"unavailable",controller.signal.aborted?504:503,true);}finally{clearTimeout(timer);}
 }
 health(){return this.#request("GET","/health",v=>healthResponseSchema.parse(v));}
 curriculum(){return this.#request("GET","/v1/curriculum",v=>curriculumResponseSchema.parse(v));}
 search(input:unknown){const p=searchInputSchema.parse(input);return this.#request("GET",`/v1/search?query=${encodeURIComponent(p.query)}&limit=${p.limit}`,v=>searchResponseSchema.parse(v));}
 source(turnId:string){const id=sourceIdSchema.parse(turnId);return this.#request("GET",`/v1/sources/${id}`,v=>sourceResponseSchema.parse(v));}
 context(input:unknown){const p=contextInputSchema.parse(input);return this.#request("POST","/v1/context",v=>contextResponseSchema.parse(v),p);}
}
