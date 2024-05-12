package main

import (
	"context"

	"github.com/LucaBazzea/private_pin_server/database"

	"github.com/gofiber/fiber/v2"
)

func hello_world(context *fiber.Ctx) error {
	return context.SendString("Hello World")
}

// Will take user ID as an input
func user(context *fiber.Ctx) error {
	user := make(map[string]interface{})
	user["id"] = 42
	user["name"] = "Emanuele"
	user["lat"] = 45.47546505
	user["lon"] = 9.17875954

	return context.JSON(user)
}

// Will take group ID as an input
func group(context *fiber.Ctx) error {
	var group []map[string]interface{}

	user1 := map[string]interface{}{
		"id":   34,
		"name": "Giulia",
		"lat":  45.48546505,
		"lon":  9.18875954,
	}
	group = append(group, user1)

	user2 := map[string]interface{}{
		"id":   38,
		"name": "Roberto",
		"lat":  45.48546505,
		"lon":  9.18875954,
	}
	group = append(group, user2)

	user3 := map[string]interface{}{
		"id":   24,
		"name": "Enzo",
		"lat":  45.46646505,
		"lon":  9.26675954,
	}
	group = append(group, user3)

	return context.JSON(group)
}

func main() {
	database.ConnectDb()
	app := fiber.New()

	app.Get("/", hello_world)

	app.Get("/user_location", user_location)

	app.Listen(":3000")
}
