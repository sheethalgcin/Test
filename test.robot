*** Settings ***
Library    DateTime

*** Keywords ***
#Adding Set Date to run the telemetry validation with github actions.
#This function uses from and to values the command line arguments if its given else it will validate for 24 hours.
Set date
    log to console     ${VAR1}
    log to console     ${VAR2}        
    ${Start}    get variable value    ${from}
    ${end}      get variable value    ${to}
    IF  '${Start}' == '${None}' or '${end}' == '${None}'
        ${current_time}    Get Current Date    result_format=%Y-%m-%d %H:%M:%S
        ${twenty_four_hours_ago}    Subtract Time From Date    ${current_time}    24 hours
        ${Start}    convert date    ${twenty_four_hours_ago}    %Y-%m-%dT%H:%M:%SZ
        ${End}      convert date   ${current_time}      %Y-%m-%dT%H:%M:%SZ
        set test variable    $from      ${Start}
        set test variable    $to      ${End}
        log to console   ${from}
        log to console   ${to}
    END

*** Test Cases ***
Test the robot suite
    [Tags]  Telemetry
    [Documentation]  Runs Setdat 
    Set date  
