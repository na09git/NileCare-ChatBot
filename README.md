🤖 NileCare ChatBot: Your Personal Health Assistant 🩺
NileCare ChatBot is an intelligent, user-friendly virtual assistant designed to provide quick, reliable, and accessible health support to our community. Whether you're looking to 📅 book a medical appointment, get 📚 trusted health information, or explore 💻 NileCare’s services, our chatbot is here to help — anytime, anywhere 🌐.

🌐 chat.niletech.co  
🌐 chat.vercel.app

✨ Key Features:
🕒 24/7 Availability: Get health support at your convenience, without waiting in queues.
👨‍⚕️ Doctor Booking Made Easy: Schedule online consultations or in-person visits with qualified doctors in just a few steps.
🧠 Health Awareness: Receive daily health tips, disease prevention advice, and wellness content in local languages 🌍.
🗣️ Multilingual Support: Communicate in your preferred language for better clarity and comfort.
⚡ Instant Responses: Quick answers to frequently asked health questions to save you time.
🧑‍💻 Human Support Option: Need more help? The chatbot connects you to a live support agent when necessary.

💡 Why NileCare ChatBot?
NileCare ChatBot empowers users to take control of their health with confidence and ease 💪. By combining technology 🤖 with compassion ❤️, NileCare is transforming how communities access healthcare — bridging the gap between doctors and patients with smart, efficient, and inclusive solutions 🌱

# NILECARE - End-to-end-Medical-Chatbot-Generative-AI

# How to run?

### STEPS:

Clone the repository

```bash
Project repo: https://github.com/
```

### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n medibot python=3.10 -y
```

```bash
conda activate medibot
```

### STEP 02- install the requirements

```bash
pip install -r requirements.txt
```

### Create a `.env` file in the root directory and add your Pinecone & openai credentials as follows:

```ini
PINECONE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
OPENAI_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

```bash
# run the following command to store embeddings to pinecone
python store_index.py
```

```bash
# Finally run the following command
python app.py
```

Now,

```bash
open up localhost:
```

### Techstack Used:

- Python
- LangChain
- Flask
- GPT
- Pinecone

# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

    #with specific access

    1. EC2 access : It is virtual machine

    2. ECR: Elastic Container registry to save your docker image in aws


    #Description: About the deployment

    1. Build docker image of the source code

    2. Push your docker image to ECR

    3. Launch Your EC2

    4. Pull Your image from ECR in EC2

    5. Lauch your docker image in EC2

    #Policy:

    1. AmazonEC2ContainerRegistryFullAccess

    2. AmazonEC2FullAccess

## 3. Create ECR repo to store/save docker image

    - Save the URI: 970547337635.dkr.ecr.ap-south-1.amazonaws.com/medicalchatbot

## 4. Create EC2 machine (Ubuntu)

## 5. Open EC2 and Install docker in EC2 Machine:

    #optinal

    sudo apt-get update -y

    sudo apt-get upgrade

    #required

    curl -fsSL https://get.docker.com -o get-docker.sh

    sudo sh get-docker.sh

    sudo usermod -aG docker ubuntu

    newgrp docker

# 6. Configure EC2 as self-hosted runner:

    setting>actions>runner>new self hosted runner> choose os> then run command one by one

# 7. Setup github secrets:

- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY
- AWS_DEFAULT_REGION
- ECR_REPO
- PINECONE_API_KEY
- OPENAI_API_KEY
