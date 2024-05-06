package main

import (
	"github.com/LucaBazzea/private_pin_server/database"

	"github.com/gofiber/fiber/v2"
)

func hello_world(context *fiber.Ctx) error {
	return context.SendString("Hello World")
}

func user_location(context *fiber.Ctx) error {
	user := make(map[string]interface{})
	user["id"] = 42
	user["name"] = "Emanuel"
	user["lat"] = 45.47546505
	user["lon"] = 9.17875954

	return context.JSON(user)
}

func main() {
	database.ConnectDb()
	app := fiber.New()

	app.Get("/", hello_world)

	app.Get("/user_location", user_location)

	app.Listen(":3000")
}
