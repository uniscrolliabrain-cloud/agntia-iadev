import {Hono,type Context} from "hono";
import {KnowledgeClient,KnowledgeError} from "./client.js";
/** Host must authenticate the session and authorize knowledge.read before resolving a client. */
export function knowledgeRoutes(resolve:(c:Context)=>Promise<KnowledgeClient>){
 const app=new Hono();app.use("*",async(c,next)=>{c.header("Cache-Control","no-store");await next();});
 app.get("/curriculum",async c=>c.json(await(await resolve(c)).curriculum()));
 app.get("/search",async c=>{const q=c.req.query();if(Object.keys(q).some(k=>!["query","limit"].includes(k)))return c.json({code:"validation"},422);return c.json(await(await resolve(c)).search({query:q.query,limit:q.limit===undefined?10:Number(q.limit)}));});
 app.get("/sources/:id",async c=>c.json(await(await resolve(c)).source(c.req.param("id"))));
 app.post("/context",async c=>c.json(await(await resolve(c)).context(await c.req.json())));
 app.onError((e,c)=>{const err=e instanceof KnowledgeError?e:new KnowledgeError("unavailable",503);return c.json({code:err.kind,retryable:err.retryable},err.status as 400|401|403|404|422|429|502|503|504);});
 return app;
}
