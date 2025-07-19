## SRC format
Create 3 folder/files:
1. server.js
2. router.js
3. controller.js
   
### Server
1. Import express
```bash
import express from 'express';
```

2. Setup dotenv and port
```bash
dotenv.config()
const PORT = process.env.port || 5000
```

3. Setup app
```bash
const app = express()
app.use(express.json())
```

4. Setup routes
```bash
import <routeObject> from "<routeFile>";
app.use("<routeRootURL>", <routeObject>)
```
Note: repeat app.use for each routeObject

5. Start server
```bash
app.listen(PORT, () => {
  <configurations>;
  console.log("Server started at htt://localhost:" + PORT);
}
```
Note: example of configurations, `connectDB()`. Remember to import first.

### Routes

