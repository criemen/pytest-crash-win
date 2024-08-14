#!/bin/bash -e

# call gh api to run workflow dispatch


for i in {1..10}
do
    GH_PAGER= gh api -X POST /repos/:owner/:repo/actions/workflows/reproduce-windows.yml/dispatches -f ref=main
done
