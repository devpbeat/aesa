'use strict';

/**
 * plain controller
 */

const { createCoreController } = require('@strapi/strapi').factories;

module.exports = createCoreController('api::plain.plain');
