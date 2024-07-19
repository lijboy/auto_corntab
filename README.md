# URL Visitor

This project uses GitHub Actions to periodically visit a specified URL and log the results.

## Setup

1. Fork this repository.
2. Go to your forked repository's Settings > Secrets and variables > Actions.
3. Add a new repository secret named `TARGET_URL` with the URL you want to visit.
4. The GitHub Action will now run automatically every 6 hours, or you can manually trigger it from the Actions tab.

## Files

- `.github/workflows/schedule.yml`: Defines the GitHub Actions workflow.
- `main.py`: The Python script that visits the URL and logs the result.
- `requirements.txt`: Lists the Python dependencies.

## Customization

- To change the schedule, modify the `cron` expression in `schedule.yml`.
- To change what data is logged or how it's processed, modify `main.py`.

## Logs

You can view the logs for each run in the Actions tab of your GitHub repository.
