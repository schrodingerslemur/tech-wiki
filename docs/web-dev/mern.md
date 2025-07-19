### Starting a web dev project
```bash
npm init -y
npm i express mongoose dotenv
npm i nodemon -D
```
#### Tips for better project layout
In package.json:
1. Add `"type": "module"` to allow for import '<function>' from '<module>'
2. Add `"scripts": {"dev": "nodemon <filename>"}` for e.g. `"scripts": {"dev": "nodemon scripts/backend.js"}

#### Frontend
```bash
mkdir frontend
cd frontend
```
Follow instructions at (react-wiki)[https://github.com/schrodingerslemur/tech-wiki/blob/main/docs/web-dev/react.md]

#### Backend
Follow instructions at:
1. (express-wiki)[https://github.com/schrodingerslemur/tech-wiki/blob/main/docs/web-dev/express.md]
2. (mongo-wiki)[https://github.com/schrodingerslemur/tech-wiki/blob/main/docs/web-dev/mongo.md]
