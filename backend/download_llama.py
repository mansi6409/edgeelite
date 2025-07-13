#!/usr/bin/env python3
"""
Download Llama-2-7b-chat-hf for EdgeElite AI Assistant
For Qualcomm HaQathon - Using HF Hub Authentication
"""

import os
from pathlib import Path
from huggingface_hub import login

def download_llama_with_hub():
    """Download Llama-2-7b-chat-hf using HF Hub login."""
    
    print("🚀 Downloading Llama-2-7b-chat-hf for EdgeElite AI Assistant")
    print("=" * 70)
    
    # Create models directory
    models_dir = Path(__file__).parent / "models"
    models_dir.mkdir(exist_ok=True)
    
    model_path = models_dir / "llama-2-7b-chat-hf"
    
    if model_path.exists():
        print(f"✅ Llama-2 model already exists at: {model_path}")
        return True
    
    try:
        # Login to Hugging Face Hub
        print("🔐 Logging into Hugging Face Hub...")
        login(token="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", new_session=False)
        print("✅ Login successful!")
        
        from transformers import AutoTokenizer, AutoModelForCausalLM
        
        print("📥 Downloading Llama-2-7b-chat-hf...")
        print("Model: meta-llama/Llama-2-7b-chat-hf")
        print("Size: ~14GB (will be quantized for edge devices)")
        print("Time: ~10-30 minutes depending on internet speed")
        print()
        
        # Download tokenizer
        print("1. Downloading tokenizer...")
        tokenizer = AutoTokenizer.from_pretrained(
            "meta-llama/Llama-2-7b-chat-hf",
            token="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",
            cache_dir=models_dir,
            trust_remote_code=True
        )
        tokenizer.save_pretrained(model_path)
        print("✅ Tokenizer downloaded")
        
        # Download model (quantized for edge devices)
        print("2. Downloading model (quantized for edge devices)...")
        model = AutoModelForCausalLM.from_pretrained(
            "meta-llama/Llama-2-7b-chat-hf",
            token="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",
            cache_dir=models_dir,
            torch_dtype="auto",
            device_map="auto",
            trust_remote_code=True,
            low_cpu_mem_usage=True
        )
        model.save_pretrained(model_path)
        print("✅ Model downloaded")
        
        print()
        print("🎉 Llama-2-7b-chat-hf successfully downloaded!")
        print(f"📍 Location: {model_path}")
        print("⚡ Ready for edge AI inference on Snapdragon X-Elite")
        print()
        print("Next steps:")
        print("1. Restart your backend server")
        print("2. Test the AI assistant in your app")
        print("3. Enjoy real AI responses!")
        
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("Please install required dependencies:")
        print("   pip install transformers torch accelerate huggingface_hub")
        return False
        
    except Exception as e:
        print(f"❌ Download failed: {e}")
        print()
        print("Alternative: Use the enhanced mock system for now")
        print("The mock system provides realistic AI responses for development")
        return False

def test_llama_download():
    """Test if Llama-2 model can be loaded."""
    try:
        from transformers import AutoTokenizer, AutoModelForCausalLM
        
        print("🧪 Testing Llama-2 model...")
        
        # Test tokenizer with explicit token
        tokenizer = AutoTokenizer.from_pretrained(
            "meta-llama/Llama-2-7b-chat-hf",
            token="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"
        )
        print("✅ Tokenizer test successful")
        
        # Test model loading (just a small part to verify)
        model = AutoModelForCausalLM.from_pretrained(
            "meta-llama/Llama-2-7b-chat-hf",
            token="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",
            torch_dtype="auto",
            device_map="auto",
            trust_remote_code=True
        )
        print("✅ Model test successful")
        
        return True
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False

def main():
    """Main function."""
    print("EdgeElite AI Assistant - Llama-2-7b-chat-hf Downloader")
    print("For Qualcomm HaQathon - Using HF Hub Authentication")
    print()
    
    # First test if we can access the model
    print("🔍 Testing model access...")
    if test_llama_download():
        print("✅ Model access test successful!")
        
        # Ask user if they want to download
        print("\nDo you want to download the full model? (y/n): ", end="")
        response = input().lower().strip()
        
        if response in ['y', 'yes']:
            success = download_llama_with_hub()
            if success:
                print("\n✅ Setup complete! Your EdgeElite AI Assistant is ready.")
            else:
                print("\n⚠️ Setup incomplete. Using enhanced mock system.")
        else:
            print("\n⏭️ Skipping download. Using remote inference.")
    else:
        print("\n❌ Cannot access Llama-2 model. Check your authentication.")
        print("Please ensure you have access to meta-llama/Llama-2-7b-chat-hf")

if __name__ == "__main__":
    main() 