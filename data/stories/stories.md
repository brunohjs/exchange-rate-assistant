## start
* start
  - action_greet
  - action_menu

## exchange_rate
* greet
  - action_greet
  - action_menu
* exchange_rate
  - action_exchange_rate

## conversion
* greet
  - action_greet
  - action_menu
* conversion
 - action_conversion
* show_conversion
 - action_show_conversion

## currency_list
* greet
  - action_greet
  - action_menu
* currency_list
  - action_currency_list

## explanation
* greet
  - action_greet
  - action_menu
* explanation
  - action_explanation
* affirm OR negate
  - action_menu

## farewell
* greet
  - action_greet
  - action_menu
* farewell
  - action_farewell

## menu
* menu
 - action_menu

## help
* help
 - action_help
 - action_menu

## happy path
* greet
  - action_greet
  - action_menu
* exchange_rate
  - action_exchange_rate
* conversion
  - action_conversion
* show_conversion
  - action_show_conversion
* farewell
  - action_farewell

## out_of_scope
* out_of_scope
  - action_default_fallback