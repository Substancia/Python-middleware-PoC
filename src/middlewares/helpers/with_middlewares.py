def with_middlewares(handler, middlewares: list):
    def modified_handler(event, context):
        def chain_middlewares(middlewares_list: list):
            if len(middlewares_list) == 0:
                return handler

            first_middleware = middlewares_list[0]
            rest_of_middlewares = middlewares_list[1:]

            def nest_middlewares(e, c):
                return first_middleware(e, c, chain_middlewares(rest_of_middlewares))
            
            return nest_middlewares
        
        try:
            return chain_middlewares(middlewares)(event, context)
        except Exception as err:
            return err

    return modified_handler