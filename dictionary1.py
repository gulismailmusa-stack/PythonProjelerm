#key:value

#istanbul=>34
#rize=>53

#sehirler=["istanbul","rize"]
#plakalar=["34","53"]

#print(sehirler[1],plakalar[0])
#print(sehirler[0],plakalar[1])

#print(sehirler[1][plakalar])

rehber={
"sadık turan":{
"12345",
"435453"
}
"cınar turan":{
"ev":"98765",
"is":"0394833",
"cep":"34232123"
"mahalle":{"sehir":"kocaeli",
"cadde":"sümüne sokak.",
"no":35
}
}
}
print(rehber["sadık turan"][ev])
print(rehber["cınar turan"][cep])
print(rehber["sadık turan"][is],[cep])
print(rehber["cınar turan"][mahalle][sehir])
sehirler={ "istanbul"
          plaka:"34",
"rize"
plaka:"43",
"kocaeli"
plaka:"41",
}
print(sehirler["kocaeli"][plaka])
print(sehirler["rize"][plaka])
print(sehirler["istanbul"][plaka])
