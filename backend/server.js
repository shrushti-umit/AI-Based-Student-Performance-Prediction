const express = require("express");
const cors = require("cors");

const app = express();

app.use(cors());

app.use(express.json());

app.post("/api/chat",(req,res)=>{

    const {prompt}=req.body;

    res.json({
        reply:"Server received : "+prompt
    });

});

app.listen(5000,()=>{
    console.log("Server Running");
});
