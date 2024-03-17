package main

import (
	"github.com/LucaBazzea/private_pin_server/database"

	"github.com/gofiber/fiber/v2"
)

func hello_world(context *fiber.Ctx) error {
	return context.SendString("Hello World")
}

func main() {
	database.ConnectDb()
	app := fiber.New()

	app.Get("/", hello_world)

	app.Listen(":3000")
}
