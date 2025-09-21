import express from "express";
import dotenv from "dotenv"
import cors from "cors";
import { connectDB } from "./config/db.js";
import router from "./route.product.js";
const app=express();
app.use(express.json());
app.use(cors());
app.use("/api/products",router);

dotenv.config();
app.listen(5000,()=>{
    connectDB();
    console.log("server started at port http://localhost:5000");
});