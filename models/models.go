package models

import "time"

type User struct {
	ID       uint64  `json:"id" gorm:"primary_key"`
	Username string  `json:"username" gorm:"not null"`
	Email    string  `json:"email" gorm:"not null"`
	Lat      float32 `json:"lat"`
	Lon      float32 `json:"lon"`
	Created  time.Time
}
