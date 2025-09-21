import express from "express"
import products from "./models/product.js"
const router=express.Router();
router.put("/:id",async (req,res)=>{
    try{
        const {id}=req.params;
        const product=req.body;
        const updatedProduct=await products.findByIdAndUpdate(id,product,{new:true})
        res.status(200).json({success:true,data:updatedProduct});

    }catch(e){
        console.log(e);
        res.status(500).json({success:false,message:"server error"});

    }
});


router.get("/",async (req,res)=>{
    try{
        const allProducts=await products.find({});
        res.status(200).json({success:true,data:allProducts});
    }catch(e){
        res.status(500).json({success:true,message:"Server Error"})
        console.log(e)
    }
});


router.post("/",async (req,res)=>{
    const product=req.body;
    if(!product.name||!product.price||!product.image){
        return res.status(400).json({success:false,message:"please provide all fields"})
    }
    const newProduct= new products(product);
    try{
        newProduct.save();
        res.status(201).json({success:true,data:newProduct});
    }catch(e){
        console.error(`Error in create product:${e.message}`)
        res.status(500).json({success:false,message:"server error"})
    }
});

router.delete("/:id", async (req,res)=>{
    const {id}=req.params;
    try{
    await products.findByIdAndDelete(id);
    res.status(200).json({success:true,message:"product has been deleted"});
}catch(e){
    console.error("error:",e.message);
    res.json({success:false,message:"product not found"});
}
});
export default router;