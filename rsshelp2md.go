package main

import (
	"fmt"
	"os"
	"path/filepath"
	"strings"

	md "github.com/JohannesKaufmann/html-to-markdown"
	"github.com/JohannesKaufmann/html-to-markdown/plugin"
	gofeed "github.com/mmcdole/gofeed"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {

	file, _ := os.Open("./input/help.combined.rss")
	defer file.Close()
	fp := gofeed.NewParser()

	feed, _ := fp.Parse(file)
	fmt.Println(feed.Items[0].GUID)
	converter := md.NewConverter("", true, nil)
	converter.Use(plugin.GitHubFlavored())

	outputDir := filepath.Join(".", "export")
	err := os.MkdirAll(outputDir, os.ModePerm)
	check(err)

	for _, item := range feed.Items {
		markdown, err := converter.ConvertString(item.Content)
		check(err)

		out := "---"
		out += "\ntitle: " + item.Title
		out += "\ncategories: " + strings.Join(item.Categories, ",")
		out += "\n---"
		out += "\n\n" + markdown

		mdFilename := item.GUID + ".md"
		mdFilepath := filepath.Join(outputDir, mdFilename)
		err = os.WriteFile(mdFilepath, []byte(out), 0644)
		check(err)
	}
}
