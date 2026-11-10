
# Integrante responsável: Reny Costa

from playwright.sync_api import Page, expect


def test_apresentacao_tela_login(page: Page):
    page.goto("https://local-eats-unisenac.vercel.app/")

    expect(page.get_by_role("link", name="LocalEats")).to_be_visible()

    expect(page.get_by_text("Bem-vindo ao app de Qualidade de Software")).to_be_visible()

    campo_email = page.get_by_role("textbox",name="teste@teste.com")

    expect(campo_email).to_be_visible()

    campo_email.fill("teste@teste.com")

    expect(campo_email).to_have_value("teste@teste.com")

    botao_entrar = page.locator("#loginForm").get_by_role("button", name="Entrar")

    expect(botao_entrar).to_be_visible()
