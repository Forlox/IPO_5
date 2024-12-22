import requests as r

with open("API_key.txt", "r") as file: #токен берется из .txt файла первой строки
      token = file.readline().strip()
      print("===Токен успешно загружен.===")

user = "Forlox"
repo = "IPO_5"
org = "freeCodeCamp"

print()
while True:
      print(f"1. Вывод репозиториев организации\n"
            f"2. Вывод репозиториев пользователя\n"
            f"3. Вывод репозитория пользователя\n"
            f"4. Создание репозитория\n"
            f"5. Удаление репозитория\n")
      inp = int(input("Выберите действие: "))

      if inp == 1:
            check_repos = r.get(f"https://api.github.com/orgs/{org}/repos").json()
            for obj in check_repos:
                  name = obj['name']
                  id = obj['id']
                  print(f"Репозитория: {name}\nid: {id}")

      elif inp == 2:
            check_repos_user = r.get(f"https://api.github.com/users/{user}/repos").json()
            for obj in check_repos_user:
                  name = obj['name']
                  id = obj['id']
                  print(f"Репозитория: {name}\nid: {id}")
            print()

      elif inp == 3:
            check_repo = r.get(f"https://api.github.com/repos/{user}/{repo}", auth=(user, token)).json()
            print(f"Репозитория: {check_repo['name']} и id: {check_repo['id']}\n")

      elif inp == 4:
            description = "Создание репозитория через python"
            data = {
                  "name": repo,
                  "description": description,
            }
            create_repo = r.post("https://api.github.com/user/repos", auth=(user, token), json=data)
            print(create_repo.status_code)
            if create_repo.status_code == 201:
                  print("Репозиторий успешно создан!\n")
            else:
                  print("Не получилось создать репозиторий!\n")

      elif inp == 5:
            delete_repo = r.delete(f"https://api.github.com/repos/{user}/{repo}", auth=(user, token))
            if delete_repo.status_code == 204:
                print("Удаление прошло успешно!\n")
            else:
                  print("Репозиторий не удалён!\n")

      else:
            print("Некорректный ввод.")
