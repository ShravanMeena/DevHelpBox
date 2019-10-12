package main

import (
	"encoding/json"
	"io"
	"log"
	"net/http"
	"strconv"

	"github.com/gorilla/mux"
)

// Cat structure type (object)
type Cat struct {
	ID   int    `json:"id"`
	Name string `json:"name"`
	Age  int    `json:"age"`
	Pic  string `json:"pic"`
}

// Dog structure type (object)
type Dog struct {
	ID   int    `json:"id"`
	Name string `json:"name"`
	Age  int    `json:"age"`
	Pic  string `json:"pic"`
}

var cats = []Cat{
	Cat{ID: 1, Name: "Lemon", Age: 3, Pic: "https://images2.minutemediacdn.com/image/upload/c_crop,h_1193,w_2121,x_0,y_175/f_auto,q_auto,w_1100/v1554921998/shape/mentalfloss/549585-istock-909106260.jpg"},
	Cat{ID: 2, Name: "Lyra", Age: 8, Pic: "https://www.petmd.com/sites/default/files/Senior-Cat-Care-2070625.jpg"},
	Cat{ID: 3, Name: "Howl", Age: 5, Pic: "https://img.washingtonpost.com/wp-apps/imrs.php?src=https://img.washingtonpost.com/rf/image_960w/2010-2019/WashingtonPost/2016/05/05/Interactivity/Images/iStock_000001440835_Large1462483441.jpg&w=1484"},
	Cat{ID: 4, Name: "Faraday", Age: 3, Pic: "http://r.ddmcdn.com/s_f/o_1/cx_462/cy_245/cw_1349/ch_1349/w_720/APL/uploads/2015/06/caturday-shutterstock_149320799.jpg"},
	Cat{ID: 5, Name: "Monet", Age: 1, Pic: "https://s.marketwatch.com/public/resources/images/MW-HP036_CatOnC_ZH_20190808094806.jpg"},
	Cat{ID: 6, Name: "Olive", Age: 10, Pic: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQdMIU_4V4XtUAiV2uOBmeixkhQuy6N3eaHH1XuUzOYFyQZBZefEg"},
	Cat{ID: 7, Name: "Ramen", Age: 4, Pic: "https://static.scientificamerican.com/sciam/cache/file/32665E6F-8D90-4567-9769D59E11DB7F26_source.jpg?w=590&h=800&7E4B4CAD-CAE1-4726-93D6A160C2B068B2"},
}

var dogs = []Dog{
	Dog{ID: 1, Name: "Adna", Age: 7, Pic: "http://www.dictionary.com/e/wp-content/uploads/2018/05/doggo-300x300.jpg"},
	Dog{ID: 2, Name: "Kata", Age: 10, Pic: "https://i.ytimg.com/vi/7NYaGOyJiCY/maxresdefault.jpg"},
	Dog{ID: 3, Name: "Newton", Age: 2, Pic: "http://www.notinthedoghouse.com/wp-content/uploads/2014/02/dog-with-closed-eyes.jpg"},
	Dog{ID: 4, Name: "Faraday", Age: 9, Pic: "https://i.pinimg.com/originals/a2/07/78/a207785ece9d08a17326f9709207f0a8.jpg"},
	Dog{ID: 5, Name: "Hoss", Age: 15, Pic: "https://cdn2-www.dogtime.com/assets/uploads/gallery/finnish-spitz-dogs-and-puppies/finnish-spitz-dogs-puppies-1.jpg"},
	Dog{ID: 6, Name: "Franklin", Age: 1, Pic: "https://static.independent.co.uk/s3fs-public/thumbnails/image/2019/09/04/13/istock-1031307988.jpg?w968h681"},
}

func catsHandler(w http.ResponseWriter, req *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(cats)
}

func catHandler(w http.ResponseWriter, req *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	params := mux.Vars(req)
	id, _ := strconv.Atoi(params["id"])
	for _, cat := range cats {
		if cat.ID == id {
			json.NewEncoder(w).Encode(cat)
			return
		}
	}
	w.WriteHeader(http.StatusNotFound)
}

func dogsHandler(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(dogs)
}

func dogHandler(w http.ResponseWriter, req *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	params := mux.Vars(req)
	id, _ := strconv.Atoi(params["id"])
	for _, dog := range dogs {
		if dog.ID == id {
			json.NewEncoder(w).Encode(dog)
			return
		}
	}
	w.WriteHeader(http.StatusNotFound)
}

func testHandler(w http.ResponseWriter, req *http.Request) {
	io.WriteString(w, "Hello, Mux!\n")
}

func indexHandler(w http.ResponseWriter, req *http.Request) {
	http.ServeFile(w, req, "static/index.html")
}

func funPageHandler(w http.ResponseWriter, req *http.Request) {
	http.ServeFile(w, req, "static/contact.html")
}

func main() {
	r := mux.NewRouter()
	r.HandleFunc("/", indexHandler).Methods("GET")
	r.HandleFunc("/test", testHandler).Methods("GET")
	r.HandleFunc("/index", indexHandler).Methods("GET")
	r.HandleFunc("/cats", catsHandler).Methods("GET")
	r.HandleFunc("/cats/{id:[0-9]+}", catHandler).Methods("GET")
	r.HandleFunc("/dogs", dogsHandler).Methods("GET")
	r.HandleFunc("/dogs/{id:[0-9]+}", dogHandler).Methods("GET")
	r.HandleFunc("/func", funPageHandler)
	http.Handle("/", r)
	log.Fatal(http.ListenAndServe(":8080", nil))
}
