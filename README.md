# Project Overview

Our project aims to develop an Employee Management System (EMS) using natural language processing (NLP) techniques. We initially attempted to fine-tune a Hugging Face model to generate SQL queries for our MongoDB database. However, due to the complexity of our nested schema, we shifted our approach to using a pre-trained Hugging Face model that converts English prompts into SQL queries effectively.

## Key Achievements:
- **Model Training**: We manually created prompts and SQL data to fine-tune our Hugging Face model. This approach proved challenging due to the complexity of our schema.
- **Schema Generation**: We successfully integrated our custom schema with the pre-trained model, enabling it to generate SQL queries tailored to our domain.
- **Frontend Development**: We developed a basic frontend interface with login and signup functionalities, along with a user-friendly GUI for our EMS.

## Next Steps:
- Integrate the prompt to sql generator model into our frontend interface.
- Integrate the EMS with MySql for efficient data storage and retrieval.
- Enhance the frontend design and user experience based on feedback.
