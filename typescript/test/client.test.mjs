import test from "node:test";
import assert from "node:assert/strict";
import {KnowledgeClient,KnowledgeError} from "../dist/index.js";
const opts={baseUrl:"http://localhost:8000/",approvedOrigins:["http://localhost:8000"],credential:()=>"x".repeat(32)};
test("rejects unapproved origin",()=>assert.throws(()=>new KnowledgeClient({...opts,approvedOrigins:["https://elsewhere.example"]}),KnowledgeError));
test("parses curriculum",async()=>{
 const client=new KnowledgeClient({...opts,fetch:async()=>new Response(JSON.stringify({nodes:[{id:"intro"}]}),{headers:{"content-type":"application/json"}})});
 assert.equal((await client.curriculum()).nodes[0].id,"intro");
});
test("validates search query",async()=>{
 const client=new KnowledgeClient({...opts,fetch:async()=>new Response(JSON.stringify({hits:[]}),{headers:{"content-type":"application/json"}})});
 await assert.rejects(client.search({query:""}));
 assert.deepEqual((await client.search({query:"RAG"})).hits,[]);
});
test("rejects malformed response",async()=>{
 const client=new KnowledgeClient({...opts,fetch:async()=>new Response(JSON.stringify({unexpected:true}),{headers:{"content-type":"application/json"}})});
 await assert.rejects(client.curriculum(),e=>e.kind==="contract");
});
test("passes server bearer token",async()=>{
 let authorization="";
 const client=new KnowledgeClient({...opts,fetch:async(_url,init)=>{authorization=init.headers.Authorization;return new Response(JSON.stringify({status:"ok",llm_configured:false}),{headers:{"content-type":"application/json"}});}});
 await client.health();assert.equal(authorization,"Bearer "+"x".repeat(32));
});
