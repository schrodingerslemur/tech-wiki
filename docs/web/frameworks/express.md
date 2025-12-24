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
  <config functions>;
  console.log("Server started at htt://localhost:" + PORT);
}
```
Note: example of config functions, `connectDB()`. Remember to import config functions first.

### Routes
1. Import express
2. Create router
```bash
const router = express.Router()
```
3. Import controllers
e.g. `import { getProducts, createProduct, ... } from 'controller.js'`
4. Define routes
e.g.
```bash
router.post("/", createProduct);
router.delete("/:id", deleteProduct);
```
5. Export router
```bash
export default router;
```

### Controllers
1. Import necessary config and libraries (e.g. mongoose, or database models)
2. Define controller functions (e.g. database interactions)
e.g.
```bash
export const getProducts = async (req, res) => {
   try {
   }
   catch (error) {
   }
```
##### HTTP Methods
- Get: retrieve data
- Post: create data
- Put: update entire data
- Patch: update part of data
- Delete: delete data

#### Requests:
Get requests by using
```bash
const requestJson = req.body;
```
Or if request was passed through url (e.g. "/:id")
```bash
const { id } = req.params;
```

#### Responses:
Return responses using
```bash
res.status(<status code>).json({ <json message> })
```
##### Status codes:
- 200: Ok - generic status
- 201: Created - on successful POST
- 204: No Content - on successful DELETE
- 400: Bad request - missing/invalid input
- 404: Not found - resource not found
- 500: Internal server error - unhandled exception
- 502: Bad gateway - invalid response upstream
- 503: Service unavailable - down or overloaded server

  
