"""
Complete training script - adds ALL data properly
"""
from database import SessionLocal, LinkedInPost, ProfileData

db = SessionLocal()

# Clear existing
print("🗑️  Clearing database...")
db.query(LinkedInPost).delete()
db.query(ProfileData).delete()
db.commit()

print("=" * 70)
print(" TRAINING THE AI MODEL")
print("=" * 70)

# Run existing scripts
print("\n📚 Adding viral training examples...")
import subprocess
subprocess.run(["python", "train_model.py"], check=True)
subprocess.run(["python", "add_batch3.py"], check=True)
subprocess.run(["python", "add_batch4.py"], check=True)

print("\n👤 Adding your profile...")
subprocess.run(["python", "add_saad_profile.py"], check=True)

print("\n" + "=" * 70)
print(" ✅ TRAINING COMPLETE!")
print("=" * 70)

# Final stats
db2 = SessionLocal()
training_count = db2.query(LinkedInPost).filter(
    LinkedInPost.post_type == "training_example"
).count()

user_count = db2.query(LinkedInPost).filter(
    LinkedInPost.post_type == "user_profile"
).count()

print(f"\n📊 Total Training Data:")
print(f"   • Viral examples: {training_count} posts")
print(f"   • Your posts: {user_count} posts")
print(f"   • TOTAL: {training_count + user_count} posts")

print("\n🚀 Start generating content:")
print("   python simple_main.py")
print("=" * 70)

db2.close()
