interface Config {
    development: DefaultConfig;
    production: DefaultConfig;
    test: DefaultConfig;
}

interface DefaultConfig {
    destinationAddress: string;
    projectId: string;
}

const config = require('./config.json') as Config;
const environment =  process.env.NODE_ENV || 'development';
const environmentConfig = config[environment];
export default environmentConfig;
