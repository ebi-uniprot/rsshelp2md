#!/usr/bin/env bash
declare -a arr=(
	"uniprotkb"
	"uniref"
	"uniparc"
	"proteomes"
	"taxonomy"
	"keywords"
	"citations"
	"diseases"
	"database"
	"locations"
	"id-mapping"
	"unirule"
	"arba"
)

for namespace in "${arr[@]}"
do
   echo "$namespace"
   curl -s https://rest.uniprot.org/beta/configure/$namespace/result-fields | jq '..|.name? | strings' | tr -d '"' > $namespace.result-fields.txt
done

cat *result-fields.txt | sort | uniq > all.txt 