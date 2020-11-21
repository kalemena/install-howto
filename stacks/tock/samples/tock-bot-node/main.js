
const { Bot } = require('tock-node');

const bot = new Bot('9437c8e6-a493-41e9-9b28-9a922bbf6c2f', 'bot_api', 8080, 'ws');

bot.addStory('allumer la lumière', bot => {
  console.log("allumer lumière");
  bot.send("j'allume la lumière");
//  bot.end('Comment puis-je aider ?');
});

bot.addStory('allumer', (bot, request) => {
  console.log("intent allumer");
  // getting user context
  console.log(bot.userData);
  // user message
  console.log(request.message.text);
  // entities
  console.log(request.entities);
  // answer
  bot.send("j'allume la lumière");
//  bot.end('Comment puis-je aider ?');
});

bot.addStory('greeting',  (bot, request) => {
  console.log("intent greeting/bonjour");
  // getting user context
  console.log(bot.userData);
  // user message
  console.log(request.message.text);
  // entities
  console.log(request.entities);
  // answer
  bot.send("que puis-je pour vous ?");
//  bot.end('Comment puis-je aider ?');
});

//     newStory("qui-es-tu") { // Answer for the 'qui-es-tu' story
//                send("Je suis un assistant conversationnel construit avec Tock")
//                end("Comment puis-je aider ?")
//            }

