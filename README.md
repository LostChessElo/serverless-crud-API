# Table of Contents

- [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Tech Stack](#tech-stack)
  - [Badges I've earned through AWS Edcucate](#badges-ive-earned-through-aws-edcucate)
  - [Architecture](#architecture)
  - [API endpoints and request routing](#api-endpoints-and-request-routing)
  - [Project structure](#project-structure)
---
## Overview

A serverless REST API for managing notes, built and deployed on AWS. It supports full CRUD operations (create, read, update, and delete) over a `/notes` endpoint.

The architecture is fully managed and pay-per-use:

- **AWS Lambda** runs the application code (Python), scaling automatically with demand.
- **Amazon DynamoDB** is the NoSQL database, storing records in a `notes` table.
- **API Gateway** exposes the REST endpoints and triggers the Lambda function on each request.
- **IAM** secures the stack, providing the Lambda execution role and an OIDC role for keyless deployments from CI/CD.
- **CloudWatch** captures logs and metrics for observability.
- **AWS Budgets** guards against unexpected cost, with an alert configured to trigger on any spend above $0.01.

---
## Tech Stack
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

---
## Badges I've earned through AWS Edcucate  

<p>
  <a href="https://www.credly.com/badges/7c5df9be-3099-4fcf-a46b-58fde3d85f0f/public_url">
    <img src="https://images.credly.com/size/110x110/images/3b1b42e6-dfc2-492b-90df-8058096cb93d/blob" alt="AWS Educate: Getting Started with Storage" width="150" />
  </a>
  <a href="https://www.credly.com/badges/bd83d1f8-79bf-49a8-b0ab-24ca19da1e0b/public_url">
    <img src="https://images.credly.com/size/110x110/images/e51a8579-188d-4363-8ed1-12ad164ef57b/blob" alt="AWS Educate: Getting Started with Compute" width="180" />
  </a>
  <a href="https://www.credly.com/badges/01d8f2c8-06ab-4b46-9afd-b0700727065f/public_url">
    <img src="https://images.credly.com/size/110x110/images/e50c657a-edd9-4c93-b1cf-2b6634b54abf/blob" alt="AWS Educate: Introduction to Generative AI" width="150" />
  </a>
</p>

---
[![Credly](https://img.shields.io/badge/Credly-%23FF6B00.svg?style=for-the-badge&logo=credly&logoColor=white)](https://www.credly.com/users/luke-ferley)

---
## [Architecture](https://github.com/LostChessElo/serverless-crud-API/wiki/Live-API)

<p align="center">
  <img src="docs/Architecture.drawio.svg" alt="Serverless Notes API architecture" width="800" />
</p>

---

## API endpoints and request routing 

| Method | Path           | Description                     | Request Body                                  | Success Response          |
|--------|----------------|---------------------------------|-----------------------------------------------|---------------------------|
| GET    | `/notes`       | Return all notes                | None                                             | `200` : array of notes    |
| POST   | `/notes`       | Create a note                   | `{ "name": string, "description": string }` : `name` required | `201` : created note      |
| PATCH  | `/notes/{id}`  | Update a note's fields          | `{ "name"?: string, "description"?: string }` : both optional; empty body returns note unchanged | `200` : updated note      |
| DELETE | `/notes/{id}`  | Delete a note                   | None                                             | `200` : delete confirmation |

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Project structure

```code
serverless-crud-API/
├── .github/
│   └── workflows/
│       ├── ci.yml              # lint, typecheck, test on push/PR
│       └── cd.yml              # zip src/ -> update Lambda (manual approval)
├── .vscode/
│   └── settings.json           # editor config (analysis extraPaths)
├── docs/
│   └── Architecture.drawio.svg # architecture diagram
├── src/                        # Lambda code to be zipped and deployed
│   ├── app.py                  # dispatcher: routes by httpMethod
│   ├── get_handler.py
│   ├── post_handler.py
│   ├── patch_handler.py
│   ├── delete_handler.py
│   ├── db.py                   # DynamoDB table handle
│   └── response.py             # ok()/error() response helpers
├── tests/
│   ├── conftest.py             # mock DynamoDB fixtures
│   ├── test_get.py
│   ├── test_delete.py
│   └── test_validation.py
├── .gitignore
├── .python-version             # pins interpreter
├── pyproject.toml              # deps and tool config 
├── uv.lock                     # locked deps
└── README.md
```

WeThinkCode_ LMS: WTC-J6ECFL2N