package main

import (
	"fmt"
)


type CacheMemory struct {
	UserData   interface{} 
	UserAction interface{}
	AiData     interface{}
	AiAction   interface{}
}

func cache_builder(cache []string) CacheMemory {
	var tmp_cache []interface{} 
	var cache_construct CacheMemory

	for _, value := range cache {
		tmp_cache = append(tmp_cache, value)
	}

	if len(tmp_cache) == 4 {
		cache_construct = CacheMemory{
			UserData:   tmp_cache[0],
			UserAction: tmp_cache[1],
			AiData:     tmp_cache[2],
			AiAction:   tmp_cache[3],
		}
	} else {
		fmt.Println("Warning: cache does not contain exactly 4 elements")
	}

	return cache_construct

}