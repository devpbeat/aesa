'use strict';

/**
 * plain service
 */

const { createCoreService } = require('@strapi/strapi').factories;

module.exports = createCoreService('api::plain.plain');
