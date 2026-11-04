# Laboratorium 5 – kontrola dostępu w Apache i CGI

Uruchomienie (w katalogu z compose.yaml):

    docker compose build web
    docker compose up -d web
    docker compose exec web httpd -t

Baza haseł (lokalnie, nie w repozytorium):

    docker compose run --rm --no-deps narzedzia -cB /auth/uzytkownicy student

Moje pliki:
- konfiguracja/dostep.conf – reguły dostępu (zadania 1–3)
- cgi-bin/uprawnienia.cgi – program CGI (zadanie 3)
