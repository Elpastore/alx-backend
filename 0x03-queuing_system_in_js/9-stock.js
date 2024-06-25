const express = require('express');
//const { createClient } = require('redis');
//const { promisify } = require('util');
import { createClient } from 'redis';
import { promisify } from 'util';

const port = 1245;
const app = express();

const client = createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.error('Redis client not connected to the server:', err);
});

const getAsync = promisify(client.get).bind(client);

const listProducts = [
  { itemId: 1, itemName: 'Suitcase 250', price: 50, initialAvailableQuantity: 4 },
  { itemId: 2, itemName: 'Suitcase 450', price: 100, initialAvailableQuantity: 10 },
  { itemId: 3, itemName: 'Suitcase 650', price: 350, initialAvailableQuantity: 2 },
  { itemId: 4, itemName: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5 }
];

function getItemById(id) {
  return listProducts.find(item => item.itemId === id);
}

function reserveStockById(itemId, stock) {
  client.set(`item.${itemId}`, stock);
}

async function getCurrentReservedStockById(itemId) {
  try {
    const reservedStock = await getAsync(`item.${itemId}`);
    return reservedStock;
  } catch (error) {
    console.error('Error:', error);
  }
}

app.get('/list_products', (request, response) => {
  response.json(listProducts);
});

app.get('/list_products/:itemId', async (request, response) => {
  const itemId = parseInt(request.params.itemId);
  const item = getItemById(itemId);

  if (item) {
    const stock = await getCurrentReservedStockById(itemId);
    const resItem = {
      itemId: item.itemId,
      itemName: item.itemName,
      price: item.price,
      initialAvailableQuantity: item.initialAvailableQuantity,
      currentQuantity: stock !== null ? parseInt(stock) : item.initialAvailableQuantity
    };
    response.json(resItem);
  } else {
    response.json({ status: "Product not found" });
  }
});

app.get('/reserve_product/:itemId', async (request, response) => {
  const itemId = parseInt(request.params.itemId);
  const item = getItemById(itemId);

  if (!item) {
    response.json({ status: "Product not found" });
    return;
  }

  let currentStock = await getCurrentReservedStockById(itemId);

  if (currentStock !== null) {
    currentStock = parseInt(currentStock);
    if (currentStock > 0) {
      reserveStockById(itemId, currentStock - 1);
      response.json({ status: "Reservation confirmed", itemId: itemId });
    } else {
      response.json({ status: "Not enough stock available", itemId: itemId });
    }
  } else {
    reserveStockById(itemId, item.initialAvailableQuantity - 1);
    response.json({ status: "Reservation confirmed", itemId: itemId });
  }
});

app.listen(port, () => {
  console.log(`App listening at http://localhost:${port}`);
});
