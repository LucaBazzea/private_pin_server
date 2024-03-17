package database

import (
	"log"
	"os"

	"gorm.io/driver/sqlite"
	"gorm.io/gorm"
	"gorm.io/gorm/logger"

	"github.com/LucaBazzea/private_pin_server/models"
)

type DbInstance struct {
	Db *gorm.DB
}

var Database DbInstance

func ConnectDb() {
	db, error := gorm.Open(sqlite.Open("private_pin.db"), &gorm.Config{})

	if error != nil {
		log.Fatal("DB Connection Failed \n", error.Error())
		os.Exit(2)
	}

	log.Println("DB Connection Success")
	db.Logger = logger.Default.LogMode(logger.Info)

	log.Println("Running Migrations")
	db.AutoMigrate(&models.User{})

	Database = DbInstance{Db: db}
}
