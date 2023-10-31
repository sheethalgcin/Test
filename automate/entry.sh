#!/bin/bash

# Set and export environment variables based on conditions
if [ "$CONDITION1" = "true" ]; then
  export VAR1="IOS"
  export VAR2="APPLE"
elif [ "$CONDITION2" = "true" ]; then
  export VAR1="Web"
  export VAR2="WebApp"
else
  export VAR1="Android"
  export VAR2="Mobile"
fi

# Run the Robot Framework tests with the chosen environment variables
robot --variable VAR1:$VAR1 --variable VAR2:$VAR2 -d  output --output  output.xml  --xunit  res.xml  Tests/verify/*
#robot  test.robot  # Replace with the actual path to your Robot Framework tests
