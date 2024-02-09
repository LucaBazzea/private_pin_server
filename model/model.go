

type User struct {
	ID       uint64 `json:"id" gorm:"primary_key"`
	Username string `json:"username" gorm:"not null"`
	Email    string `json:"email" gorm:"not null"`
	Lat      string `json:"lat"`
	Lon      string `json:"lon"`
}
