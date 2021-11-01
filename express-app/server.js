const express = require('express')
const app = express()
const hostname = process.env.HOSTNAME || "localhost"
const port = process.env.PORT || 3000

app.get('/', (req, res) => {
  res.send("Welcome to Express!!!")
})

app.listen(port, () => {
  console.log(`Example express app listening at http://${hostname}:${port}`)
})