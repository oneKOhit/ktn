import json
from MessageReceiver import MessageReceiver


class MessageParser():
    def __init__(self):
        self.possible_responses = {
            'error': self.parse_error,
            'info': self.parse_info,
            'message': self.parse_message,
            'history': self.parse_history
        }

    def parse(self, payload):
        try:
            if payload['response'] in self.possible_responses:
                return self.possible_responses[payload['response']](payload)
            else:
                return "Response not valid"
        except Exception as e:
            print("")

    def parse_error(self, payload):
        return "[Error]" + str(payload['content'])

    def parse_info(self, payload):
        return "[Info] " + str(payload['content'])

    def parse_message(self, payload):
        return "[" + str(payload["timestamp"]) + " - " + str(payload['sender']) + "] " + str(payload["content"]) 

    def parse_history(self, payload):
        history = "\n"
        for message in payload['content']:
            parser = MessageParser()
            history += parser.parse(message) + "\n"
        return history