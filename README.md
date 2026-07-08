# Overview
A serverless CRUD notes taking API deployed with AWS.
###### 
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![boto3](https://img.shields.io/badge/boto3-232F3E?style=flat&logo=amazonwebservices&logoColor=white)
![pytest](https://img.shields.io/badge/pytest-0A9EDC?style=flat&logo=pytest&logoColor=white)
![moto](https://img.shields.io/badge/moto-8A2BE2?style=flat&logo=python&logoColor=white)
![AWS Lambda](https://img.shields.io/badge/AWS%20Lambda-FF9900?style=flat&logo=awslambda&logoColor=white)
![API Gateway](https://img.shields.io/badge/API%20Gateway-FF4F8B?style=flat&logo=amazonapigateway&logoColor=white)
![DynamoDB](https://img.shields.io/badge/DynamoDB-4053D6?style=flat&logo=amazondynamodb&logoColor=white)
![CloudWatch](https://img.shields.io/badge/CloudWatch-FF4F8B?style=flat&logo=amazonwebservices&logoColor=white)
![IAM](https://img.shields.io/badge/IAM-DD344C?style=flat&logo=amazonwebservices&logoColor=white)
![AWS Budgets](https://img.shields.io/badge/AWS%20Budgets-232F3E?style=flat&logo=amazonwebservices&logoColor=white)
## Table of Contents

- [Overview](#overview)
  - [Table of Contents](#table-of-contents)
  - [Badges I've earned through AWS Edcucate](#badges-ive-earned-through-aws-edcucate)
  - [API endpoints and request routing](#api-endpoints-and-request-routing)
---
## Badges I've earned through AWS Edcucate  

<p>
  <a href="https://www.credly.com/badges/7c5df9be-3099-4fcf-a46b-58fde3d85f0f/public_url">
    <img src="https://images.credly.com/size/110x110/images/3b1b42e6-dfc2-492b-90df-8058096cb93d/blob" alt="AWS Educate: Getting Started with Storage" width="100" />
  </a>
  <a href="https://www.credly.com/badges/bd83d1f8-79bf-49a8-b0ab-24ca19da1e0b/public_url">
    <img src="https://images.credly.com/size/110x110/images/e51a8579-188d-4363-8ed1-12ad164ef57b/blob" alt="AWS Educate: Getting Started with Compute" width="100" />
  </a>
</p>

[![Credly](https://img.shields.io/badge/Credly-%23FF6B00.svg?style=for-the-badge&logo=credly&logoColor=white)](https://www.credly.com/users/luke-ferley)

---
## API endpoints and request routing 

| Method | Path           | Description                     | Request Body                                  | Success Response          |
|--------|----------------|---------------------------------|-----------------------------------------------|---------------------------|
| GET    | `/notes`       | Return all notes                | None                                             | `200` : array of notes    |
| POST   | `/notes`       | Create a note                   | `{ "name": string, "description": string }` : `name` required | `201` : created note      |
| PATCH  | `/notes/{id}`  | Update a note's fields          | `{ "name"?: string, "description"?: string }` : both optional; empty body returns note unchanged | `200` : updated note      |
| DELETE | `/notes/{id}`  | Delete a note                   | None                                             | `200` : delete confirmation |
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
