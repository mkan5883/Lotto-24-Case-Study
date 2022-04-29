from behave import *


@given(u'A visitor is on the wikipedia home page')
def step_impl(context):
    context.driver.get("https://en.wikipedia.org/")
    assert context.home_page.get_home_page_title() == "Welcome to Wikipedia"


@when(u'The visitor searches for "{search}"')
def step_impl(context, search):
    context.home_page.enter_search_keyword(search)
    context.home_page.click_search_button()


@then(u'A ‘did you mean’ suggestion is displayed')
def step_impl(context):
    assert context.search_page.verify_did_u_mean_suggestion_is_visible()


@then(u'The visitor can see "{count}" results')
def step_impl(context, count):
    assert context.search_page.get_suggestion_count() == count


@given(u'A visitor is on the search result page for "{search}"')
def step_impl(context, search):
    assert context.search_page.verify_search_result_page(search)


@when(u'The visitor uses the “Did you mean” feature to correct his search')
def step_impl(context):
    context.search_page.click_did_you_mean_suggestion()


@when(u'And select the first entry')
def step_impl(context):
    context.search_suggestion = context.search_page.click_search_suggestion(0)


@then(u'The visitor is on the article page of the first hit')
def step_impl(context):
    title = context.article_page.get_article_title()
    assert context.search_suggestion == title
