import zipfile

zip_path = "arquivo.zip"  # <-- troque pelo seu arquivo ZIP

senhas_para_testar = [
    "luiz",
    "lampreia",
    "luizlampreia",
    "luiz_lampreia",
    "lampreia_luiz",

    "llampreia",
    "luizl",
    "llamp",
    "lampreial",
    "luizl123",

    "luiz123",
    "luiz1234",
    "luiz2024",
    "luiz2025",
    "lampreia123",
    "lampreia2024",
    "lampreia2025",
    "luizlampreia123",
    "luizlampreia2024",

    "luiz!",
    "luiz@123",
    "luiz#2024",
    "lampreia!",
    "lampreia@2024",
    "luiz_lampreia!",
    "luiz-lampreia@123",

    "Luiz",
    "Lampreia",
    "LuizLampreia",
    "LUIZLAMPREIA",
    "LuizLampreia2024",

    "luizsenha",
    "senhaLuiz",
    "luizmeu123",
    "luizpass",
    "lampreia123!"
]

with zipfile.ZipFile(zip_path) as z:
    for senha in senhas_para_testar:
        try:
            print(f"Testando: {senha}")
            z.extractall(pwd=senha.encode())
            print(f"\n SENHA ENCONTRADA: {senha}\n")
            break
        except:
            pass
    else:
        print("\nNenhuma das senhas da lista funcionou.\n")
