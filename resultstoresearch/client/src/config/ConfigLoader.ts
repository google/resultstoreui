interface DefaultConfig {
    destinationAddress: string;
    projectId: string;
    clientId: string;
}

const environmentConfig: DefaultConfig = {
    destinationAddress:
        process.env.REACT_APP_ENVOY_ADDRESS || 'http://localhost:8090',
    clientId:
        process.env.REACT_APP_CLIENT_ID ||
        '835513274128-siubdukq9bv1rjq6fv3vvglf4eukte7m.apps.googleusercontent.com',
    projectId:
        process.env.REACT_APP_PROJECT_ID || 'google.com:gchips-productivity',
};

export default environmentConfig;
