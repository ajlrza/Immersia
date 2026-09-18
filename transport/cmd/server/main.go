package main

import (
     "fmt"
     "log"
     "github.com/gofiber/fiber/v3"
     "net/url"
     //"net/http"
)
type InteractionMetadata struct {
    EventWhen string
    GraphMasterID int // Master identifier responsible for placing the interaction data
    GraphNodes int // How many graph nodes, used for optimizing and storing properly
    StatesAffected int // How many states affected, used also for optimizing and compress
    EngineStatus string // Engine status as of this interaction
}

type UpdatedStruct struct {
    Action string
    Avatar uint32
    Position uint32
    World string
}

type EnginePayload struct {
    Action string
    Avatar string 
    Position uint32
    World string 
    Metadata InteractionMetadata
}

type EngineResponse struct {
    Context string
    UpdatedStruct UpdatedStruct
    ByteData uint32
}

type PromptPayload struct {
    Prompt string
    Metadata string
    Key string
    Model string
}

type PacketHeader struct {
    Version uint8   
    Type    uint8   
    Length  uint16  
    ID      uint32 
}

// func EngineExtendor(ExtendedState ...)

func main() {
     
     app := fiber.New()

     //networkClient := &http.Client{}

     app.Get("/", func(c fiber.Ctx) error {
        return c.SendString("Go Lang TEST 👋!")
     })

     app.Post("/interact", func(c fiber.Ctx) error {

        if !c.HasBody() {
            return c.SendStatus(fiber.StatusBadRequest)
        }

        body := c.Body()
        req_url := c.FullURL()

    })

     app.Post("/cache-memory", func(c fiber.Ctx) error {

        if !c.HasBody() {
            return c.SendStatus(fiber.StatusBadRequest)
        }
     
        body := c.Body()
        u, err := url.Parse(c.FullURL())

        if err != nil {
            return c.SendStatus(fiber.StatusBadRequest) 
        }

        userId := u.Query().Get("userid") 

        if userId == "" {
            fmt.Println("User not found in the request... attemping to ask the client.")
            ask_unknown_user := map[string]any{
                "Unknown": true,
            }

            return c.JSON(ask_unknown_user)
        }

        var memory_cache = cache_builder()

    })

     log.Fatal(app.Listen(":3000"))
     fmt.Println("Server sarted at https://localhost/3000")
}