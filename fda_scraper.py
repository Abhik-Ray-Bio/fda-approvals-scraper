on:
  schedule:
    - cron: '0 9 * * *'
  workflow_dispatch:  # This enables manual "Run workflow" button
  push:
    branches: [ main ]
