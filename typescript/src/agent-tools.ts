import type {KnowledgeClient} from "./client.js";
/** Read-only tools. Host runtime must authorize capability and provide a scoped client. */
export const KNOWLEDGE_READ_CAPABILITIES=[
 {id:"iadev.curriculum.tree",version:"1.0.0",sideEffects:[],retryable:true},
 {id:"iadev.knowledge.search",version:"1.0.0",sideEffects:[],retryable:true},
 {id:"iadev.knowledge.source",version:"1.0.0",sideEffects:[],retryable:true},
 {id:"iadev.knowledge.context",version:"1.0.0",sideEffects:[],retryable:true},
] as const;
export function knowledgeTools(client:()=>Promise<KnowledgeClient>){
 return {
  "iadev.curriculum.tree":{description:"Read the learning curriculum",inputSchema:{type:"object",properties:{},additionalProperties:false},execute:async()=> (await client()).curriculum()},
  "iadev.knowledge.search":{description:"Search the education corpus",inputSchema:{type:"object",properties:{query:{type:"string"},limit:{type:"integer",minimum:1,maximum:50}},required:["query"],additionalProperties:false},execute:async(input:{query:string;limit?:number})=>(await client()).search(input)},
  "iadev.knowledge.source":{description:"Retrieve a cited conversation turn",inputSchema:{type:"object",properties:{turnId:{type:"string"}},required:["turnId"],additionalProperties:false},execute:async(input:{turnId:string})=>(await client()).source(input.turnId)},
  "iadev.knowledge.context":{description:"Prepare cited, untrusted educational context",inputSchema:{type:"object",properties:{query:{type:"string"}},required:["query"],additionalProperties:false},execute:async(input:{query:string})=>(await client()).context(input)},
 };
}
