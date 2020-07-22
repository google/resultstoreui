import React, { useState } from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import FilePage from './Pages/FilePage';
import Home from './Pages/HomePage';
import FlakyTest from './Pages/FlakyTestPage';
import { AuthContext, TokenId } from './contexts/AuthContext';

function App() {
    const [tokenId, setTokenId] = useState<TokenId>('');
    return (
        <AuthContext.Provider value={{ tokenId, setTokenId }}>
            <Router>
                <Switch>
                    <Route exact path="/">
                        <Home />
                    </Route>
                    <Route exact path="/file" component={FilePage} />
                    <Route exact path="/flaky-test" component={FlakyTest} />
                </Switch>
            </Router>
        </AuthContext.Provider>
    );
}

export default App;
