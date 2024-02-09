package database

import (
	"log"

	"gorm.io/gorm"
	"gorm.io/gorm/logger"
)

type DbInstance struct {
	Db *gorm.DB
}

var Database DbInstance

func ConnectDb() {
  db, error : gorm.Open(sqlite.Open("private_pin.db"), &gorm.Config{})

  if error != nil {
    log.Fatal("DB Connection Failed \n", err.Error())
    os.Exit(2)
  }

  log.Println("DB Connection Success")
  db.Logger = logger.Default.LogMode(logger.Info)
}

type User struct {
	ID       uint64 `json:"id" gorm:"primary_key"`
	Username string `json:"username" gorm:"not null"`
	Email    string `json:"email" gorm:"not null"`
	Lat      string `json:"lat"`
	Lon      string `json:"lon"`
}
