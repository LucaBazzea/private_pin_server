package main

import (
	"github.com/gofiber/fiber/v2"
)

func hello_world(context *fiber.Ctx) error {
	return context.SendString("Hello World")
}

func main() {
	app := fiber.New()

	app.Get("/", hello_world)

	app.Listen(":3000")
}
