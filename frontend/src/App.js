import React, { Component } from 'react';

const todoItems = [
  {
    id: 1,
    title: "Go to Market",
    description: "Buy ingredients to prepare dinner",
    completed: true,
  },
  {
    id: 2,
    title: "Study",
    description: "Read Algbra and History textbook for the upcoming test",
    completed: false,
  },
  {
    id: 3,
    title: "Sammy's books",
    description: "Go to library to return ",
    completed: false,
  },
  {
    id: 4,
    title: "Article",
    description: "Write article on how to use Django with React",
    completed: false,
  },

]

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      viewCompleted: false,
      todoList: todoItems,
    };
  }

  displayCompleted = (status) => {
    if (status) {
      return this.setState({ viewCompleted: true });
    }

    return this.setState({ viewCompleted: false });
  };

  renderTabList = () => {
    return (
        <div className="nav nav-tabs">
          <span
              className={this.state.viewCompleted ? "nav-link active" : "nav-link"}
              onClick={() => this.displayCompleted(true)}
          >
            Complete
          </span>
          <span
              className={this.state.viewCompleted ? "nav-link" : "nav-link active"}
              onClick={() => this.displayCompleted(false)}
          >
            Incomplete
          </span>
        </div>
    );
  };

  renderItems = () => {

  };

}
