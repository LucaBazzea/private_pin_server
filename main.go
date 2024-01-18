package main

import (
  "github.com/gofiber/fiber"
)

func hello_world(context *fiber.Ctx) {
  context.Send("Hello World")
}

func main() {
  app := fiber.New()

  app.Get("/", hello_world)

  app.Listen(3000)
}
