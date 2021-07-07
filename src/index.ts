import Parser from "rss-parser";
import fs from "fs";
import path from "path";
import TurndownService from "turndown";

type CustomFeed = {
  lastBuildDate: string;
};

type Category = { $: { term: string } }[];

type CustomItem = {
  title: string;
  id: string;
  link: string;
  updated: string;
  category: Category;
  content: string;
};

const parser: Parser<CustomFeed, CustomItem> = new Parser({
  customFields: {
    feed: ["lastBuildDate"],
    item: [
      ["category", "category", { keepArray: true }],
      ["updated", "updated"],
    ],
  },
});

const turndownService = new TurndownService();

const categoriesMap: Partial<{ [key: string]: string[] }> = {};

const parseCategory = (category: Category): string[] =>
  category.map((cat) => Object.values(cat.$)).flat();

(async () => {
  fs.readFile(
    path.join(__dirname, "../input/help.combined.rss"),
    "utf8",
    async (error, data) => {
      const parsed = await parser.parseString(data);

      parsed.items.forEach((item) => {
        const markdown = turndownService.turndown(item.content);
        const content = `
---
title: ${item.title}
categories: ${parseCategory(item.category).join(",")}
---

${markdown}
        `;

        fs.writeFile(
          path.join(__dirname, `../export/${item.id}.md`),
          content,
          (error) => console.error(error?.message)
        );
        // This generates an object of categories => articles
        item.category.forEach((catObj) => {
          const catName = catObj["$"]["term"];
          if (categoriesMap[catName]) {
            categoriesMap[catName]?.push(item.title);
          } else {
            categoriesMap[catName] = [item.title];
          }
        });
      });
    }
  );
})();
