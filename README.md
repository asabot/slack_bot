# slack_bot
A few Flask based Slack bots for team fun!

Setup:
 1. git clone https://github.com/asabot/slack_bot
 2. Create and source python venv :
   * pip install virtualenv
   * virtualenv venv
   * source venv/bin/activate
  3. Create a slack-api tokens. 
    * [Go to slack's web api](https://api.slack.com/web)
    * Scroll down and click generate token.
    * Export this token as OS environmental variable: SLACK_TOKEN
    * Add all the slack integrations you plan to use from this bot sweat (your-team.slack.com/apps/manage) and export them as their coresonding OS envvironmental variables.
    * Resource your enviroment and then resource the venv.
  4. Route the webhook from slack to your server.
  5. Run the Flask app!
     * Depending on where you routed the webhook, you may have to change recieve.py to run somewhere else (default is 0.0.0.0:5000
     * In terminal type: python recieve.py
